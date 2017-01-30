<script>
var map = new ol.Map({
    target: '{{uuid}}',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([{{longitude}}, {{latitude}}]),
      zoom: {{zoom}}
    })
});
</script>
