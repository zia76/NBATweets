(function() {
  var addAccessor, root;

  addAccessor = function(obj, name, value) {
    return obj[name] = function(_) {
      if (!arguments.length) {
        return obj.properties[name] || value;
      }
      obj.properties[name] = _;
      return obj;
    };
  };

  root = (typeof exports !== "undefined" && exports !== null) || this;

  root.addAccessor = addAccessor;

}).call(this);


(function() {
  var Geomap, root;

  Geomap = (function() {
    function Geomap() {
      var name, value, _ref;
      this.properties = {
        margin: {
          top: 20,
          right: 20,
          bottom: 20,
          left: 20
        },
        width: 960,
        height: 500,
        geofile: null,
        postUpdate: null,
        projection: d3.geo.naturalEarth,
        rotate: [0, 0, 0],
        svg: null,
        title: function(d) {
          return d.properties.name;
        },
        unitId: 'iso3',
        units: 'units',
        zoomMax: 1 //changed this from 4 to prevent zooming
      };
      this.properties.scale = this.properties.width / 5.8;
      this.properties.translate = [this.properties.width / 2, this.properties.height / 2];
      _ref = this.properties;
      for (name in _ref) {
        value = _ref[name];
        addAccessor(this, name, value);
      }
      this["private"] = {};
      this.selection = {};
      this.geo = {};
    }

    Geomap.prototype.clicked = function(d) {
      var centroid, geomap, k, x, x0, y, y0;
      geomap = this;
      x = null;
      y = null;
      k = null;
      if (d && geomap["private"].centered !== d) {
        centroid = geomap.properties.path.centroid(d);
        x = centroid[0];
        y = centroid[1];
        k = geomap.properties.zoomMax;
        geomap["private"].centered = d;
      } else {
        x = geomap.properties.width / 2;
        y = geomap.properties.height / 2;
        k = 1;
        geomap["private"].centered = null;
      }
      geomap["private"].g.selectAll('path').classed('active', geomap["private"].centered && function(d) {
        return d === geomap["private"].centered;
      });
      x0 = geomap.properties.width / 2;
      y0 = geomap.properties.height / 2;
      return geomap.properties.svg.selectAll('g.zoom');
      //removed to prevent panning:
      //.transition().duration(750).attr('transform', 'translate(' + x0 + ',' + y0 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')')
    };

    Geomap.prototype.update = function() {
      var geomap;
      geomap = this;
      geomap.selection.units.enter().append('path').attr('class', 'unit').attr('d', geomap.properties.path).on('click', geomap.clicked.bind(geomap)).append('title').text(geomap.properties.title);
      if (geomap.postUpdate()) {
        return geomap.properties.postUpdate();
      }
    };

    Geomap.prototype.draw = function(selection, geomap) {
      var proj;
      geomap.properties.svg = selection.append('svg').attr('width', geomap.properties.width).attr('height', geomap.properties.height);
      geomap.properties.svg.append('rect').attr('class', 'background').attr('width', geomap.properties.width).attr('height', geomap.properties.height).on('click', geomap.clicked.bind(geomap));
      geomap["private"].g = geomap.properties.svg.append('g').attr('class', 'units zoom');
      proj = geomap.properties.projection().scale(geomap.properties.scale).translate(geomap.properties.translate).precision(.1);
      if (proj.hasOwnProperty('rotate') && geomap.properties.rotate) {
        proj.rotate(geomap.properties.rotate);
      }
      geomap.properties.path = d3.geo.path().projection(proj);
      return d3.json(geomap.properties.geofile, function(error, geo) {
        geomap.geo = geo;
        geomap.selection.units = geomap["private"].g.selectAll('path').data(topojson.feature(geo, geo.objects[geomap.properties.units]).features);
        return geomap.update();
      });
    };

    return Geomap;

  })();

  root = (typeof exports !== "undefined" && exports !== null) || this;

  root.Geomap = Geomap;

  root.d3.geomap = function() {
    return new Geomap();
  };

}).call(this);
