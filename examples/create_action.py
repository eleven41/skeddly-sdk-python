import skeddly

def Main():
    client = skeddly.Client()

    try:

        # Choose one of the credentials
        credentials = client.list_credentials(
            filter = {
                "cloudProviderIds": "amazon"
            }
        )
        credentialId = credentials[0]['credentialId']

        # Create a "Start EC2 Instances" action.
        response = client.create_action(
            actionType = "amazon-start-ec2-instances",
            name = "0.Python Start EC2 Instances",
            isEnabled = True,
            schedule = {
                "scheduleType": "none",
                "startDate": "2019-01-01",
                "timeOfDay": "00:00:00",
                "timeZoneId": "Eastern Standard Time",
                "parameters": {}
            },
            parameters = {
                "CredentialIds": [
                    credentialId
                ],
                
                "instanceIdentificationMethod": "all-instances"
            }
        )

        actionId = response["actionId"]
        actionVersionId = response["actionVersionId"]
        print("Created action %s (version %s)" % (actionId, actionVersionId))

        # Modify the action
        response = client.modify_action(actionId,
            name = "0.Python Start EC2 Instances (version 2)",
            isEnabled = True,
            schedule = {
                "scheduleType": "none",
                "startDate": "2019-01-01",
                "timeOfDay": "00:00:00",
                "timeZoneId": "Eastern Standard Time",
                "parameters": {}
            },
            parameters = {
                "CredentialIds": [
                    credentialId
                ],
                
                "instanceIdentificationMethod": "all-instances"
            })

        actionVersionId = response["actionVersionId"]
        print("Action modified (new version %s)." % actionVersionId)

        # Delete the action
        client.delete_action(actionId)
        print("Action deleted.")

    except skeddly.ParameterValidationFailedException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)
        print("modelState: " + str(e.modelState))
    except skeddly.SkeddlyWebException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)


if __name__ == "__main__":
  Main()