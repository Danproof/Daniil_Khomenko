Feature: upload file with specific name

Scenario Outline: file should have defined name

    Given I upload "<file_name>" in "<dir>"

    When I get metadata of uploaded file 

    Then uploaded file has "<file_name>" name

    Examples:
        | file_name     | dir       |
        | default.jpg   | images2   |