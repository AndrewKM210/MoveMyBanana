import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:speech_recognition/speech_recognition.dart';
import 'package:coach_my_banana/util/nlpparser.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:coach_my_banana/class/mensaje.dart';
import 'dart:async';

class Chat extends StatefulWidget {
  final String nombre;

  Chat({@required this.nombre});

  @override
  _Chat createState() => _Chat(nombre);
}

class _Chat extends State<Chat> {
  final String _nombre;
  final String langCode = 'es_ES';

  Color azulSese = Color(0xFF3F48CC);

  SpeechRecognition _speech;

  bool _speechRecognitionAvailable = false;
  bool _isListening = false;

  String transcription = '';

  List<Mensaje> mensajes = List<Mensaje>();

  _Chat(this._nombre);

  ScrollController _scrollController;

  @override
  initState() {
    _scrollController = ScrollController();
    super.initState();
    activateSpeechRecognizer();
    _initSpeak();
  }

  void _openHelpDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        // return object of type Dialog
        return AlertDialog(
          title: Text("Ayuda: prueba a decir..."),
          content: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Text("* Cojo cinco mandarinas de la caja origen cuatro"),
                Text("* He dejado en destino tres tres peras"),
                Text("* Repite la última orden"),
                Text("* La caja origen cinco tiene tres peras"),
                Text("* Continuar"),
              ]),
          actions: <Widget>[
            // usually buttons at the bottom of the dialog
            new FlatButton(
              child: new Text("Close"),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  FlutterTts flutterTts = FlutterTts();

  void _initSpeak() async {
    await flutterTts.setLanguage(langCode);
    await flutterTts.setSpeechRate(1.2);
    await flutterTts.setVolume(2.0);
    await flutterTts.setPitch(1.2);
    String text = "Bienvenido, $_nombre. Di ayuda si necesitas algo.";
    await flutterTts.speak(text);
    setState(() => mensajes.add(Mensaje(mensaje: text, propio: false)));
  }

  void _speak(String frase) async {
    await flutterTts.speak("$frase");
  }

  void _easterEggDespacito() async {
    await flutterTts.setSpeechRate(0.5);
    await flutterTts.setVolume(2.5);
    await flutterTts.setPitch(2.0);
    await flutterTts.speak("Despacito tú, puto humano");
    await flutterTts.setSpeechRate(1.2);
    await flutterTts.setVolume(2.0);
    await flutterTts.setPitch(1.2);
  }

  void _easterEggCorrePlatano() async {
    await flutterTts.setSpeechRate(0.5);
    await flutterTts.setVolume(2.5);
    await flutterTts.setPitch(2.0);
    await flutterTts.speak("¡Allá va mi pomelo!");
    await flutterTts.setSpeechRate(1.2);
    await flutterTts.setVolume(2.0);
    await flutterTts.setPitch(1.2);
  }

  void parseTranscription() async {
    if (transcription.trim().isNotEmpty) {
      if (transcription.toLowerCase() == "corre plátano") {
        _easterEggCorrePlatano();
      } else if (transcription.toLowerCase() == "alexa play despacito") {
        _easterEggDespacito();
      } else {
        setState(
            () => mensajes.add(Mensaje(mensaje: transcription, propio: true)));
        String text = await NLPParser.parseTranscription(transcription);
        setState(() => mensajes.add(Mensaje(mensaje: text, propio: false)));
        _scrollController.animateTo(
          0.0,
          curve: Curves.easeOut,
          duration: const Duration(milliseconds: 300),
        );
        _speak(text);
      }
    }
  }

  static Timer queryTimer;

  void _updateTranscription() {
    if (queryTimer != null) queryTimer.cancel();
    queryTimer =
        new Timer(const Duration(milliseconds: 1000), parseTranscription);
  }

  Color getButtonColor() {
    if (_speechRecognitionAvailable && !_isListening) {
      return azulSese;
    } else if (_isListening) {
      return Colors.redAccent;
    } else {
      return azulSese;
    }
  }

  // Platform messages are asynchronous, so we initialize in an async method.
  void activateSpeechRecognizer() {
    _speech = new SpeechRecognition();
    _speech.setAvailabilityHandler(onSpeechAvailability);
    _speech.setCurrentLocaleHandler(onCurrentLocale);
    _speech.setRecognitionStartedHandler(onRecognitionStarted);
    _speech.setRecognitionResultHandler(onRecognitionResult);
    _speech.setRecognitionCompleteHandler(onRecognitionComplete);
    _speech
        .activate()
        .then((res) => setState(() => _speechRecognitionAvailable = res));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text('Operations',
              style: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center)),
      body: SafeArea(
          child: Container(
              child: Container(
                  child: Column(children: <Widget>[
        Expanded(
            child: ListView.builder(
                controller: _scrollController,
                reverse: true,
                itemCount: mensajes.length,
                itemBuilder: (context, i) {
                  Mensaje mensaje = mensajes[mensajes.length - i - 1];
                  return Container(
                      margin: EdgeInsets.all(10.0),
                      child: Container(
                          margin: EdgeInsets.only(
                              left: mensaje.propio ? 60.0 : 0.0,
                              right: mensaje.propio ? 0.0 : 60.0),
                          child: ClipRRect(
                              borderRadius: BorderRadius.circular(5.0),
                              child: Container(
                                padding: EdgeInsets.all(20.0),
                                color: mensaje.propio
                                    ? Colors.grey
                                    : (i == 0 ? azulSese : Colors.blueGrey),
                                child: Text(
                                  '${mensaje.mensaje}',
                                  style: TextStyle(
                                      fontSize: 18.0, color: Colors.white),
                                ),
                              ))));
                })),
        SizedBox.fromSize(
            size: Size(double.infinity, 100.0),
            child: Container(
                color: azulSese.withAlpha(180),
                child: Row(children: <Widget>[
                  Expanded(
                      child: Container(
                          alignment: Alignment.centerRight,
                          margin: EdgeInsets.only(left: 30.0),
                          child: RaisedButton(
                              color: azulSese,
                              padding: EdgeInsets.all(20.0),
                              onPressed: _openHelpDialog,
                              child: Icon(FontAwesomeIcons.questionCircle,
                                  color: Colors.white, size: 40.0)))),
                  Expanded(
                      child: Container(
                          alignment: Alignment.center,
                          child: RaisedButton(
                              color: azulSese,
                              padding: EdgeInsets.all(20.0),
                              onPressed: () => Navigator.pushNamed(context, '/visualizer'),
                              child: Icon(FontAwesomeIcons.chartBar,
                                  color: Colors.white, size: 40.0)))),
                  Expanded(
                      child: Container(
                          alignment: Alignment.centerLeft,
                          child: RaisedButton(
                              color: getButtonColor(),
                              padding: EdgeInsets.all(20.0),
                              onPressed: _isListening ? stop : start,
                              child: Icon(FontAwesomeIcons.dotCircle,
                                  color: Colors.white, size: 40.0))))
                ])))
      ])))),
    );
  }

  void start() => setState(() {
        _speech
            .listen(locale: langCode)
            .then((result) => print('_MyAppState.start => result $result'));
      });

  void cancel() =>
      _speech.cancel().then((result) => setState(() => _isListening = result));

  void stop() => _speech.stop().then((result) {
        setState(() => _isListening = result);
      });

  void onSpeechAvailability(bool result) {
    setState(() => _speechRecognitionAvailable = result);
  }

  void onCurrentLocale(String locale) {
    print('_MyAppState.onCurrentLocale... $locale');
    /* setState(
        () => selectedLang = languages.firstWhere((l) => l.code == locale)); */
  }

  void onRecognitionStarted() => setState(() => _isListening = true);

  void onRecognitionResult(String text) => setState(() {
        transcription = text;
      });

  void onRecognitionComplete() {
    setState(() {
      _isListening = false;
    });
    _updateTranscription();
  }

  void errorHandler() => activateSpeechRecognizer();
}
