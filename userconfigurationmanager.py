
test_settings = {
    "theme":"light",
    "volume":"medium"
}

def add_setting(settings_dict, setting_tuple):
    """
    Add a new setting to the dictionary.
    
    Args:
        settings_dict: Dictionary of settings
        setting_tuple: Tuple containing (key, value)
    
    Returns:
        Success or error message string
    """
    key, value = setting_tuple
    

    key = str(key).lower()
    
   
    value = str(value).lower()
    
   
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, setting_tuple):
    """
    Update an existing setting in the dictionary.
    
    Args:
        settings_dict: Dictionary of settings
        setting_tuple: Tuple containing (key, value)
    
    Returns:
        Success or error message string
    """
    key, value = setting_tuple

    key = str(key).lower()
    
    value = str(value).lower()

    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
def delete_setting(settings_dict, key):
    """
    Delete a setting from the dictionary.
    
    Args:
        settings_dict: Dictionary of settings
        key: Key to delete
    
    Returns:
        Success or error message string
    """
    key = str(key).lower()

    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result
