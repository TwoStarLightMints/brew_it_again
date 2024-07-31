export function remove_char_at(string, position) {
    let to_return = string.split("");

    to_return.splice(position - 1, 1);

    return to_return.join("");
}

export function validate_integer_input(event) {
    if (isNaN(event.target.value)) {
        alert("Please make sure to only enter valid integers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
    }
}

export function validate_float_input(event) {
    let validation_units = event.target.value.split(".");

    if (validation_units.filter(s => s !== "" && event.data !== "." && isNaN(s)).length != 0) {
        alert("Please make sure to only enter valid real numbers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
    } else if (validation_units.length > 2) {
        alert("Please make sure to only enter valid real numbers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
    }
}

export function validate_ratio_input(event) {
    let validation_units = event.target.value.split("/");

    if (validation_units.filter(s => s !== "" && event.data !== "/" && isNaN(s)).length != 0) {
        alert("Please make sure to only enter valid integers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
        return;
    } else if (validation_units.length > 2) {
        alert("Please make sure to only enter valid integers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
        return;
    } else if (event.target.value.length > 1 && event.target.value[1] == "0") {
        alert("You can't divide by 0!");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
        return;
    }

    if (validation_units[0].length > 1) {
        event.target.value = event.target.value[0] + "/" + event.target.value.substring(1, event.target.value.length);
    }
}

export function validate_brew_time_input(event) {
    let validation_units = event.target.value.split(":");

    if (validation_units.filter(s => s !== "" && event.data !== ":" && isNaN(s)).length != 0) {
        alert("Please make sure to only enter valid integers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
    } else if (validation_units.length > 2) {
        alert("Please make sure to only enter valid integers");
        event.target.value = remove_char_at(event.target.value, event.target.selectionStart);
    }

    if (validation_units[0].length > 1) {
        event.target.value = event.target.value[0] + ":" + event.target.value.substring(1, event.target.value.length);
    }
}
