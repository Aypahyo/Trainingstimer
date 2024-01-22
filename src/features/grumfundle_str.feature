Feature: showing off behave

  Scenario: run a simple test
     Given we have grumfundle 'foo'
      When we created a string 'foo-str' made from grumfundle 'foo' 
      Then 'foo-str' string should contain 'foo'
      And 'foo-str' string should contain 'Grumfundle'
