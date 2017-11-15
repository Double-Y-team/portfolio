$(document).ready(function () {
    var user_details = $('#user_details');
    var user_details_list = $('#user_details_list');
    console.log(user_details);
    user_details.click(function (e) {
        e.preventDefault();
    user_details_list.toggle();
    });
});