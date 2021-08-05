def post_validation_service(attrs):
    if "user" in attrs and len(attrs.get("user")) < 1:
        return "user field is required"
    elif "text" is attrs and len(attrs.get("text")):
        return "text field is required"
    else:
        return "Please provide valid data"


def report_validation_service(data):
    if "reported_by" in data and len(data.get("reported_by")) < 1:
        return "user field is required"
    elif "post" is data and len(data.get("post")):
        return "post field is required"
    else:
        return "Please provide valid data"
