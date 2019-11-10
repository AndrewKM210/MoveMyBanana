import 'package:coach_my_banana/screens/visualizer.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:coach_my_banana/screens/login.dart';
import 'package:coach_my_banana/screens/chat.dart';

class Routes {
  final routes = <String, dynamic>{
    '/': (settings) => _buildRoute(settings, new Login()),
    '/chat': (settings) => _buildRoute(
          settings,
          new Chat(nombre: settings.arguments),
        ),
    '/visualizer': (settings) => _buildRoute(settings, new Visualizer()),
  };

  Route<dynamic> _getRoute(RouteSettings settings) {
    return routes[settings.name](settings);
  }

  static MaterialPageRoute _buildRoute(RouteSettings settings, Widget builder) {
    return new MaterialPageRoute(
      settings: settings,
      builder: (ctx) => builder,
    );
  }

  Routes() {
    SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp])
        .then((_) {
      runApp(new MaterialApp(
        title: 'Move my Banana!',
        debugShowCheckedModeBanner: false,
        onGenerateRoute: _getRoute,
        initialRoute: '/',
        theme: ThemeData(
          primaryColor: Color(0xFF3F48CC),
          primaryColorLight: Color(0xFF6F74C5),
          primaryColorDark: Color(0xFF060A45),
        ),
        home: Login(),
      ));
    });
  }
}
