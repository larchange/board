<script>
    var ws = new WebSocket("ws://192.168.0.10:9000");
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
