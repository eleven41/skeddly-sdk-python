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

    def create_action(self, actionType, name, isEnabled, schedule, parameters, postExecutionTriggers = None):
        body = {
            "actionType": actionType,
            "name": name,
            "isEnabled": isEnabled,
            "schedule": schedule,
            "parameters": parameters,
            "postExecutionTriggers": postExecutionTriggers
        }

        return self.invoke_post("Actions/", body)

    def modify_action(self, actionId, name, isEnabled, schedule, parameters, postExecutionTriggers = None):
        body = {
            "name": name,
            "isEnabled": isEnabled,
            "schedule": schedule,
            "parameters": parameters,
            "postExecutionTriggers": postExecutionTriggers
        }

        return self.invoke_put("Actions/" + actionId, body)

    def delete_action(self, actionId):
        return self.invoke_delete("Actions/" + actionId)

    def execute_action(self, actionId):
        return self.invoke_put("Actions/" + actionId + "/Execute")
