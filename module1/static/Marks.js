let exam_number;
        let data_send = {};

        function handleSelectChange(selected) {
            var selected_value_select = selected.value;
            exam_number = parseInt(selected_value_select);
            var rows = document.querySelectorAll(".form-tbl tbody tr");
            rows.forEach(function(row) {
                row.cells[exam_number + 1].setAttribute(
                    'contenteditable', 'true');
            });
        };
        function prepareData() {
            var rows = document.querySelectorAll(".form-tbl tbody tr");
            rows.forEach(function(row) {
                var id_str = row.cells[1].textContent;
                var id = parseInt(id_str);
                var number = parseInt(row.cells[exam_number + 1]
                    .textContent);
                data_send[id] = number;
            });
            console.log(data_send)
        };
        var form = document.getElementById("marks_form");
        form.addEventListener("submit", function() {
            var data_through_form = document.createElement("input");
            data_through_form.type = "hidden";
            data_through_form.name = "receive";
            data_through_form.value = JSON.stringify(data_send)
            form.appendChild(data_through_form);
            let info = {'semteachid':'{{subject.id}}'}
            var extra_data = document.createElement("input");
            extra_data.type = "hidden";
            extra_data.name = "extra_info";
            extra_data.value = JSON.stringify(info)
            form.appendChild(extra_data);
        });