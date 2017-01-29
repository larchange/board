<script>
    var ws = new WebSocket("ws://" + location.hostname + ":9000");
    ws.onopen = function (event) {
        console.log("Open");
        ws.send("{{uuid}}")
    };
    ws.onmessage = function (event) {
        console.log(event.data);
        $("#{{uuid}}").html(event.data);
    };
    ws.onclose = function (event) {
        console.log("Close");
    }

</script>
