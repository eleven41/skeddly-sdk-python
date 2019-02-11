class ActionsMixin:

    # list_actions
    #
    # Returns the list of actions
    def list_actions(self, include=None, filter=None):
        queryParameters = []

        if (include is not None):
            queryParameters.append("include=" + include)
            
        if (filter is not None):
            for p in filter:
                queryParameters.append("filter." + p + "=" + filter[p])

        queryString = ""
        if (len(queryParameters) > 0):
            queryString = "?" + "&".join(queryParameters)

        return self.invoke_get("Actions" + queryString)

    def get_action(self, actionId, include=None, isIncludeDeleted=None):
        queryParameters = []

        if (include is not None):
            queryParameters.append("include=" + ",".join(include))

        if (isIncludeDeleted is not None):
            if (isIncludeDeleted):
                queryParameters.append("isIncludeDeleted=true")
            else:
                queryParameters.append("isIncludeDeleted=false")

        queryString = ""
        if (len(queryParameters) > 0):
            queryString = "?" + "&".join(queryParameters)

        return self.invoke_get("Actions/" + actionId + queryString)
