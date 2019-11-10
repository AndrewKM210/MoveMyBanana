import 'package:coach_my_banana/util/api.dart';
import 'package:coach_my_banana/class/instruccion.dart';

class NLPParser {
  static Map<String, String> mapaNumeros = {
    "uno": "1",
    "dos": "2",
    "tres": "3",
    "cuatro": "4",
    "cinco": "5",
    "seis": "6",
    "siete": "7",
    "ocho": "8",
    "nueve": "9",
    "diez": "10"
  };

  static Future<String> parseTranscription(String transcription) async {
    var phraseTo = transcription
        .toLowerCase()
        .replaceAll('á', 'a')
        .replaceAll('é', 'e')
        .replaceAll('í', 'i')
        .replaceAll('ó', 'o')
        .replaceAll('ú', 'u')
        .split(" ")
        .map((str) => mapaNumeros.containsKey(str) ? mapaNumeros[str] : str)
        .join(" ");
    Instruccion result = Instruccion(accion: 'ayuda'); // por defecto

    String accion; // cojo / dejo
    String idCaja; // O.2 o D.1
    String tipo; // platano, manzana, etc
    int cantidad; // cuantos platanos, manzanas, etc.

    String actionType;
    String target;

    RegExp re = new RegExp(r'([0-9]+) +((pera|platano|uva|pomelo|kiwi|fresa|naranja|cereza|mandarina)+s*)');
    RegExp re2 = new RegExp(r'(coj\w+|dej\w+|cog\w+)');
    RegExp re3 = new RegExp(r'((origen|destino)+(s|es)*) +([0-9]+)');
    RegExp re4 = new RegExp(r'(contin\w+|resum\w+|repet\w+|repit\w+)');
    RegExp re5 = new RegExp(r'(tien\w+|hay)');

    // FUNCIONES Take/put
    if ((re2.hasMatch(phraseTo) || re5.hasMatch(phraseTo)) &&
            re.hasMatch(phraseTo) &&
            re3.hasMatch(phraseTo)) {
      // Generacion de frases que matchean
      Match f = re.firstMatch(phraseTo);
      Match f2 = re2.firstMatch(phraseTo);
      Match f3 = re3.firstMatch(phraseTo);
      // Asignacion de variables
      cantidad = int.parse(f.group(1));
      tipo = f.group(3);
      accion = f2?.group(1) ?? re5.firstMatch(phraseTo).group(1);

      actionType = f3.group(1);
      target = f3.group(4);

      if (actionType == "origen") {
        idCaja = "O." + target;
      } else {
        idCaja = "D." + target;
      }

      if (accion.startsWith('coj') || accion.startsWith('cog')) {
        result = await API.take(idCaja, tipo, cantidad);
      } else if (accion.startsWith('dej')) {
        result = await API.put(idCaja, tipo, cantidad);
      } else if (accion.startsWith('tien') || accion.startsWith('hay')) {
        result = await API.review(idCaja, tipo, cantidad);
      }
    // FUNCION Continue
    } else if (re4.hasMatch(phraseTo)) {
      result = await API.resume();
    }

    return result.humanReadableString();
  }
}
