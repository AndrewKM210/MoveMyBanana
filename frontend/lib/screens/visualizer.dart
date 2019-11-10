import 'package:flutter/material.dart';
import 'package:coach_my_banana/class/mensaje.dart';
import 'package:coach_my_banana/util/api.dart';
import 'package:coach_my_banana/class/fruta.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class Visualizer extends StatefulWidget {
  @override
  _Visualizer createState() => _Visualizer();
}

class _Visualizer extends State<Visualizer> {
  Color azulSese = Color(0xFF3F48CC);
  static final List<Mensaje> data = [
    Mensaje(mensaje: "UNO", propio: false),
    Mensaje(mensaje: "UNO", propio: false),
    Mensaje(mensaje: "UNO", propio: false),
    Mensaje(mensaje: "UNO", propio: false),
    Mensaje(mensaje: "DOS", propio: false)
  ];

  static List<Fruta> frutas = List<Fruta>();

  static Map<String, Color> colores = {
    "platano": Colors.yellow,
    "fresa": Colors.red[200],
    "naranja": Colors.orange[600],
    "uva": Colors.purple,
    "pomelo": Colors.red[600],
    "pera": Colors.green[300],
    "kiwi": Colors.brown,
    "cereza": Colors.red,
    "mandarina": Colors.orange[300]
  };

  List<charts.Series<Fruta, String>> series = [
    charts.Series(
        id: "Subscribers",
        data: frutas,
        domainFn: (Fruta fruta, _) => fruta.id,
        measureFn: (Fruta fruta, _) => fruta.cantidad,
        colorFn: (Fruta fruta, _) =>
            charts.ColorUtil.fromDartColor(colores[fruta.name])),
  ];

  void _getProductos() async {
    List<Map<String, dynamic>> productos = await API.getData();
    productos.forEach((item) {
      if (Fruta.fromJson(item).id.startsWith('O')) {
        frutas.add(Fruta.fromJson(item));
      }
    });
    setState(() => series = [
          charts.Series(
              id: "Subscribers",
              data: frutas,
              domainFn: (Fruta fruta, _) => fruta.id,
              measureFn: (Fruta fruta, _) => fruta.cantidad,
              colorFn: (Fruta fruta, _) =>
                  charts.ColorUtil.fromDartColor(colores[fruta.name])),
        ]);
  }

  @override
  initState() {
    super.initState();
    frutas = List<Fruta>();
    _getProductos();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: azulSese,
          title: Text("Análisis de almacenes"),
        ),
        body: Center(
          child: charts.BarChart(series, animate: true),
        ));
  }
}
