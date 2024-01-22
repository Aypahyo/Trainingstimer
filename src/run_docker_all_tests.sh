#! /bin/bash
cd "$(dirname "$0")" || exit 1

container_name="testcontainer"
image_name="testimage"

function clean() {
    echo "cleaning..."
    docker stop $container_name
    docker rm $container_name
    #docker rmi $image_name
    rm test.sh.log
}

function build() {
    echo "building..."
    docker build -t $image_name -f container/dockerfile .
}

function run_tests() {
    echo "running..."
    docker run --name $container_name $image_name
    docker logs $container_name >> test.sh.log 2>&1
    docker rm -f $container_name >> test.sh.log 2>&1
    if grep -q "Tests passed: unit=0, component=0, behave=0" test.sh.log; then
        echo "-------------------"
        echo "Tests passed in docker"
        echo "-------------------"
    else
        echo "-------------------"
        echo "Tests failed in docker"
        echo "-------------------"
        exit 1
    fi
}

function run_test_for_install() {
    echo "running..."
    docker run --entrypoint "/bin/bash" --name $container_name $image_name -c "pip install . && trainingstimer --dockertest"
    local run_exit_status=$?
    docker logs $container_name >> test.sh.log 2>&1
    docker rm -f $container_name >> test.sh.log 2>&1 || true
    if grep -q "Successfully installed" test.sh.log; then
        echo "-------------------"
        echo "Install test passed in docker"
        echo "-------------------"
    else
        echo "-------------------"
        echo "Install test failed in docker"
        echo "-------------------"
        exit 1
    fi
    if [ $run_exit_status -ne 0 ]; then
        echo "-------------------"
        echo "Run test failed in docker"
        echo "-------------------"
        exit 1
    else
        echo "-------------------"
        echo "Run test passed in docker"
        echo "-------------------"
    fi
}

function main() {
    clean
    build
    run_tests
    run_test_for_install
}

main