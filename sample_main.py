import skeddly

def Main():
    client = skeddly.Client()

    try:

        # Get the list of credentials in our Skeddly account
        credentials = client.list_credentials()
        print("%d credential(s) found." % len(credentials))
        
        for c in credentials:
            credentialId = c['credentialId']
            credentialName = c['name']
            
            print("Credential: %s (%s)" % (credentialName, credentialId))
            
            # Get the actions associated with this credential
            actions = client.list_actions(
                filter={
                    "credentialIds": credentialId
                })

            # Print out each action found for this credential
            for a in actions:
                actionId = a['actionId']
                actionName = a['name']
                print("\tAction: %s (%s)" % (actionName, actionId))
            
            print("")

        

    except skeddly.ParameterValidationFailedException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)
        print("modelState: " + str(e.modelState))
    except skeddly.SkeddlyWebException as e:
        print("Error: " + str(e))
        print("ErrorCode:" + e.errorCode)


if __name__ == "__main__":
  Main()