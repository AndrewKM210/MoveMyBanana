import 'package:coach_my_banana/class/instruccion.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as json;
import 'dart:io';

class API {
  static final String ipServidor = 'http://35.180.118.1:8000';

  static Future<Instruccion> take(
      String idCaja, String tipoObjeto, int cantidad) async {
    http.Response response = await http.post('$ipServidor/take',
        headers: {
          HttpHeaders.contentTypeHeader: ContentType.json.toString(),
        },
        body: json.jsonEncode({
          "id": idCaja,
          "name": tipoObjeto,
          "quantity": cantidad,
        }));

    if (response.statusCode == 200) {
      return Instruccion.fromJson(json.jsonDecode(response.body));
    } else {
      print("Error en la API: ${response.statusCode}");
    }
    return Instruccion(accion: 'error');
  }

  static Future<Instruccion> put(
      String idCaja, String tipoObjeto, int cantidad) async {
    http.Response response = await http.post('$ipServidor/put',
        headers: {
          HttpHeaders.contentTypeHeader: ContentType.json.toString(),
        },
        body: json.jsonEncode({
          "id": idCaja,
          "name": tipoObjeto,
          "quantity": cantidad,
        }));

    if (response.statusCode == 200) {
      return Instruccion.fromJson(json.jsonDecode(response.body));
    } else {
      print("Error en la API: ${response.statusCode}");
    }
    return Instruccion(accion: 'error');
  }

  static Future<Instruccion> resume() async {
    http.Response response = await http.get(
      '$ipServidor/resume',
      headers: {
        HttpHeaders.contentTypeHeader: ContentType.json.toString(),
      },
    );

    if (response.statusCode == 200) {
      return Instruccion.fromJson(json.jsonDecode(response.body));
    } else {
      print("Error en la API: ${response.statusCode}");
    }
    return Instruccion(accion: 'error');
  }

  static Future<Instruccion> review(
      String idCaja, String tipoObjeto, int cantidad) async {
    http.Response response = await http.post('$ipServidor/review',
        headers: {
          HttpHeaders.contentTypeHeader: ContentType.json.toString(),
        },
        body: json.jsonEncode({
          "id": idCaja,
          "name": tipoObjeto,
          "quantity": cantidad,
        }));

    if (response.statusCode == 200) {
      return Instruccion.fromJson(json.jsonDecode(response.body));
    } else {
      print("Error en la API: ${response.statusCode}");
    }
    return Instruccion(accion: 'error');
  }

  static Future<List<Map<String, dynamic>>> getData() async {
    http.Response response = await http.get(
      '$ipServidor/view/product',
      headers: {
        HttpHeaders.contentTypeHeader: ContentType.json.toString(),
      },
    );

    if (response.statusCode == 200) {
      var lista = List<Map<String, dynamic>>();
      (json.jsonDecode(response.body) as List<dynamic>).forEach((item) {
        lista.add(item);
      });
      return lista;
    } else {
      print("Error en la API: ${response.statusCode}");
    }
    return List();
  }

}
