class elementLogin:
    # Login
    username = "username"
    password = "password"
    loginButton = ".oxd-button"
    verifyLogin = ".oxd-text--h6"
    invalidLogin = ".oxd-alert-content-text"
    RequiredUsername = ".oxd-form-row:nth-child(2) .oxd-text"
    RequiredPassword = ".oxd-form-row:nth-child(3) .oxd-text"
    
class pimSearch:
    sidebarPIM = "PIM"
    employeeName = "//div/div[2]/div/div/input"
    emploteeID = "//div[2]/input"
    employeeStatus = ""
    include = ""
    supervisor = ""
    jobTitle = ""
    subUnit = ""
    searchBtn = ".orangehrm-left-space"
    resetBtn = ".oxd-button--ghost"

class pimAdd:
    sidebarPIM = "PIM"
    addBtn = ".oxd-button--secondary:nth-child(1)"
    firstName = "firstName"
    middName = "middleName"
    lastName = "lastName"
    logDetile = ".oxd-switch-input"
    username = "//div[3]/div/div/div/div[2]/input"
    passwordInput = "//div[4]/div/div/div/div[2]/input"
    CpasswordInput = "//div[4]/div/div[2]/div/div[2]/input"
    saveBtn = ".oxd-button--secondary"
    cancelBtn = ".oxd-button--ghost"

class adminSearch:
    sidebarAdmin = ".active > .oxd-text"
    username = ".oxd-input--focus"
    verifUsername = ".oxd-table-cell:nth-child(2) > div"
    userRole = ".oxd-select-text--after > .bi-caret-up-fill"
    searchBtn = ".orangehrm-left-space"
    resetBtn = ".oxd-button--ghost"
    fieldEmployee = ".oxd-autocomplete-text-input > input"
    invalidMassageEmployee =".oxd-input-field-error-message"
    
class adminAdd:    
    addBtn = ".oxd-button--secondary:nth-child(1)"