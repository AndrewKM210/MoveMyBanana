class Instruccion {
  static Instruccion ultimaBuena;
  String accion;
  String name; // producto
  int quantity;
  String box;

  Instruccion({this.accion, this.name, this.quantity, this.box}) {
    if (this.accion == 'put' ||
        this.accion == 'take' ||
        this.accion == 'fin' ||
        this.accion == 'review') {
      ultimaBuena = this;
    }
  }

  Instruccion.fromJson(json)
      : this(
            accion: json['action'],
            name: json['name'],
            quantity: json['quantity'],
            box: json['box']);

  String _readableBoxName(String idBox) {
    if (idBox[0] == 'O') {
      return "origen ${idBox[2]}";
    } else {
      return "destino ${idBox[2]}";
    }
  }

  String humanReadableString() {
    switch (accion) {
      case 'take':
        return "Coge $quantity ${name == 'platano' ? 'plátano' : name}${quantity == 1 ? '' : 's'} de la caja ${_readableBoxName(box)}.";
        break;
      case 'put':
        return "Deja $quantity ${name == 'platano' ? 'plátano' : name}${quantity == 1 ? '' : 's'} en la caja ${_readableBoxName(box)}.";
        break;
      case 'error':
        return "Ha ocurrido un error de conexión con el servidor.";
        break;
      case 'review':
        return "Por favor revisa el contenido de la caja ${_readableBoxName(box)}. Di en voz alta su contenido.";
        break;
      case 'fin':
        return "No hay más operaciones por realizar.";
        break;
      default:
        return "No he entendido lo que querías decir. ${ultimaBuena != null ? ultimaBuena.humanReadableString() : ' '}";
    }
  }
}
