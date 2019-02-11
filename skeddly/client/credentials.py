
class CredentialsMixin:

    # list_credentials
    #
    # Returns the list of credentials
    def list_credentials(self, filter=None):
        queryParameters = []

        if (filter is not None):
            for p in filter:
                queryParameters.append("filter." + p + "=" + filter[p])

        queryString = ""
        if (len(queryParameters) > 0):
            queryString = "?" + "&".join(queryParameters)

        return self.invoke_get("Credentials" + queryString)

    def get_credential(self, credentialId, include=None, isIncludeDeleted=None):
        queryParameters = []

        if (isIncludeDeleted != None):
            if (isIncludeDeleted):
                queryParameters.append("isIncludeDeleted=true")
            else:
                queryParameters.append("isIncludeDeleted=false")

        queryString = ""
        if (len(queryParameters) > 0):
            queryString = "?" + "&".join(queryParameters)

        return self.invoke_get("Credentials/" + credentialId + queryString)
