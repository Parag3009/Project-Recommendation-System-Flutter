import 'package:flutter/material.dart';
import 'input_page.dart';
import 'display_page.dart'; // Make sure to import DisplayPage

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Input and Display Pages',
      initialRoute: '/',
      routes: {
        '/': (context) => InputPage(),
        '/displayPage': (context) => DisplayPage(name: ModalRoute.of(context)!.settings.arguments as String),
      },
    );
  }
}