def post_validation_service(attrs):
    if "user" in attrs and len(attrs.get("user")) < 1:
        return "user field is required"
    elif "text" is attrs and len(attrs.get("text")):
        return "Manager field is required"
    else:
        return "Please provide valid services"
