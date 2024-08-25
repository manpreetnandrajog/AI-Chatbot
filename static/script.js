
$(document).ready(function () 
{
    // Send message to backend when send button is clicked
    $('#send-button').on('click', function () {
        let userMessage = $('#message-input').val();
        if (userMessage.trim() !== '') {
            // Append user message
            $('#chat-box').append(`<div class='message user'><strong>USER:</strong> ${userMessage}</div>`);
            $('#message-input').val('');  // Clear input field

            // Ajax request to send message to backend
            $.ajax({
                url: '/chat',  // This should match your Flask route
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: userMessage }),
                success: function (response) {
                    let botMessage = response.reply;
                    // Append bot message
                    $('#chat-box').append(`<div class='message bot'><strong>BOT:</strong> ${botMessage}</div>`);
                },
                error: function (xhr, status, error) {
                    console.error("Error occurred: ", error);
                    // Append error message
                    $('#chat-box').append(`<div class='message bot'><strong>BOT:</strong> Error: Unable to contact the server.</div>`);
                }
            });
        }
    });

    // Clear chat
    $('#clear-chat').on('click', function () {
        $('#chat-box').empty();  // Clear chat box
    });

    $('#form-option').on('click', function () {
        $('#contractor-options').show();
        loadContractors('form');
    });

    $('#call-option').on('click', function () {
        $('#contractor-options').show();
        loadContractors('call');
    });

    $('#appointment-option').on('click', function () {
        $('#contractor-options').show();
        loadContractors('appointment');
    });

    function loadContractors(option) {
        $.ajax({
            url: '/contractors',
            method: 'GET',
            success: function (response) {
                let contractorsList = $('#contractors-list');
                contractorsList.empty();
                response.forEach(contractor => {
                    contractorsList.append(`
                        <div>
                            <input type="checkbox" class="contractor-select" data-id="${contractor.id}" data-name="${contractor.name}">
                            <label>${contractor.name} - ${contractor.phone}</label>
                        </div>
                    `);
                });
                $('#submit-selection').off('click').on('click', function () {
                    handleSelection(option);
                });
            }
        });
    }

    function handleSelection(option) {
        let selectedContractors = [];
        $('.contractor-select:checked').each(function () {
            selectedContractors.push($(this).data('id'));
        });

        if (option === 'form') {
            let name = prompt("Enter your name:");
            let email = prompt("Enter your email:");
            let phone = prompt("Enter your phone number:");
            $.ajax({
                url: '/fill_form',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({name: name, email: email, phone: phone, contractors: selectedContractors}),
                success: function (response) {
                    alert(response.message);
                }
            });
        } else if (option === 'call') {
            selectedContractors.forEach(id => {
                $.ajax({
                    url: '/call_contractor',
                    method: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({contractor_id: id}),
                    success: function (response) {
                        alert(response.message);
                    }
                });
            });
        } else if (option === 'appointment') {
            let appointmentTime = prompt("Enter appointment time:");
            selectedContractors.forEach(id => {
                $.ajax({
                    url: '/set_appointment',
                    method: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({contractor_id: id, appointment_time: appointmentTime}),
                    success: function (response) {
                        alert(response.message);
                    }
                });
            });
        }
    }
    $('#toggle-mode').on('click', function () {
        $('body').toggleClass('night-mode day-mode');
        $('div').toggleClass('night-mode day-mode');

        let currentMode = $('body').hasClass('night-mode') ? 'Night' : 'Day';
        $('#toggle-mode').text(`Switch to ${currentMode === 'Night' ? 'Day' : 'Night'} Mode`);
    });

    $('body').addClass('day-mode');

});
