<script>
$(document).ready(function () {
    var g = new Dygraph(
        document.getElementById("{{uuid}}"),
        "{{data_url}}"
    );
});
</script>
