Feature: upload the same name file second time

Scenario Outline: second file should not be uploaded

    Given I upload file "<file_name>" in "<dir>"

    When I upload second time file "<file_name>" in "<dir>"

    Then there is only one file "<file_name>" in "<dir>"

    Examples:
        | file_name     | dir      |
        | default.jpg   | images   |