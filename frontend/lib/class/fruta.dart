class Fruta {
  int cantidad;
  String name;
  String id;

  Fruta({this.cantidad, this.name, this.id});

  Fruta.fromJson(json)
      : this(
          cantidad: json['quantity'],
          name: json['name'],
          id: json['box'],
        );
}
