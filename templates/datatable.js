<script>
$(document).ready(function() {
    $('#{{uuid}}').DataTable({
        "ajax": "{{data_url}}",
		"processing": true,
        "serverSide": true,
        "deferRender": true,
    });
} );
</script>
