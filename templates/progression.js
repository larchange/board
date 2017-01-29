
<script>
    var ws = new WebSocket("ws://" + location.hostname + ":9000");
    ws.onopen = function (event) {
        ws.send("{{uuid}}")
    };
    ws.onmessage = function (event) {
        console.log(event.data);
        value = event.data
        $("#{{uuid}} .progress-bar").attr('aria-valuenow', value);
        $("#{{uuid}} .progress-bar").css('width', value.toString() + '%');
        $("#{{uuid}} .progress-bar").html(value.toString() + '%');
    };
    ws.onclose = function (event) {
        console.log("Close");
    }

</script>
