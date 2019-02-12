import skeddly

def Main():
    client = skeddly.Client()

    try:

        actions = client.list_actions()
        for action in actions:
            actionId = action["actionId"]
            actionName = action["name"]

            if (actionName == "Backup Virtual Machines"):
                execution = client.execute_action(actionId)
                print("Execution ID: " + execution["actionExecutionId"])


    except skeddly.ParameterValidationFailedException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)
        print("modelState: " + str(e.modelState))
    except skeddly.SkeddlyWebException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)


if __name__ == "__main__":
  Main()