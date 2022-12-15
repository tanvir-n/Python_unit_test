# Refactoring SMS Application

This task evaluates the candidate's skills in `Python 3`.

## Introduction

You are refactoring the [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product) of the SMS application written in `Python 3` for the following reasons:

  - Better testability.
  - Easier development of further providers.
  - Easier switching to new providers.
  - Greater agility.

## Problem Statement

  - Make tests pass by implementing missing features in the production code. The application is dependency-free.
  - When completing the tasks described below, rewrite functions from the `app/old.py` file into the `app/new` module using the new class structure.
  - Functions should be rewritten to classes implementing the `base` abstract class.

### Task 1

**Implement the `sms_factory` function**.

It should return the correct provider instance (`PrimarySmsApiProvider` or `SecondarySmsApiProvider`) depending on a given parameter or throw `NotImplementedError` exception if the parameter is unknown.

### Task 2

**Implement setter methods in the `BaseSmsProvider` class**.

Methods `set_content` and `set_recipient` should set a correct class attribute and should be chainable, i.e. they should return a reference to an object.

### Task 3

**Implement missing methods in the `PrimarySmsApiProvider` class**.

Create methods (responsible for validating, preparing an API payload or parsing the response) based on the `sms_primary_api` function from the `app/old.py` file.

### Task 4

**Implement the `SecondarySmsApiProvider` class**.

This task is similar to *Task 3* except for the fact, that the class `SecondarySmsApiProvider` is empty.

Make sure you take into account differences between validation rules and the payload structure between the primary and secondary API.

## Usage example

```
sms_factory('primary').set_recipient(600123456).set_content('Foo Bar').send()
```

Please find more examples inside the test cases.

## Hints

  - There are chainable methods in the app.
  - Provider methods can be found in the `app/old.py` file.
  - Instances are created using the factory design pattern.
  - The app does not include `HTTP REST SMS API`, `API` and  it’s simulated by the `fake_primary_external_api` and `fake_secondary_external_api` functions from the `app/fake.py` file.
  - You shouldn't modify the code outside of the mentioned methods.

To execute all unit tests, use:

    pip install -q -e . && python3 setup.py pytest
