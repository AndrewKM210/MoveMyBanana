import 'package:flutter/material.dart';
import 'package:permission_handler/permission_handler.dart';

class Login extends StatefulWidget {
  @override
  _Login createState() => _Login();
}

class _Login extends State<Login> {
  final _controller = TextEditingController();
  final PermissionHandler _permissionHandler = PermissionHandler();

  void _requestPermission() async {
    print("hola");
    await _permissionHandler.requestPermissions([PermissionGroup.microphone]);
  }

  @override
  initState() {
    super.initState();
    _requestPermission();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
            title: Center(
                child: Text('Move your Banana',
                    style:
                        TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
                    textAlign: TextAlign.center))),
        body: SafeArea(
            child: Container(
                child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
                margin: EdgeInsets.fromLTRB(60.0, 150.0, 60.0, 0.0),
                child: Column(children: <Widget>[
                  TextField(
                      controller: _controller,
                      decoration: InputDecoration(
                          fillColor: Colors.blueAccent,
                          hintText: 'Introduce tu nombre')),
                  Container(
                      padding: EdgeInsets.only(top: 15.0),
                      child: RaisedButton(
                          padding: EdgeInsets.symmetric(horizontal: 90.0),
                          color: Colors.blueAccent,
                          onPressed: () {
                            if (_controller.text.trim().isNotEmpty) {
                              Navigator.pushNamed(context, '/chat',
                                  arguments: _controller.text.trim());
                            }
                          },
                          child: Text(
                            'Entrar',
                            style:
                                TextStyle(color: Colors.white, fontSize: 18.0),
                          )))
                ])),
            Expanded(
              child: Container(
                  alignment: Alignment.bottomRight,
                  child: Image.asset('assets/banana.gif')),
            )
          ],
        ))));
  }
}
