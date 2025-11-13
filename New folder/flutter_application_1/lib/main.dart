import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final seed = ColorScheme.fromSeed(
      seedColor: const Color.fromARGB(255, 0, 67, 11),
    );
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: seed,
        useMaterial3: true, // ensures widgets follow the ColorScheme
        appBarTheme: AppBarTheme(
          backgroundColor: seed.inversePrimary,
          foregroundColor: seed.onInverseSurface,
        ),
        floatingActionButtonTheme: FloatingActionButtonThemeData(
          backgroundColor: seed.primary,
          foregroundColor: seed.onPrimary,
        ),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text('Two buttons centered below:'),
            const SizedBox(height: 16),
            Row(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                FloatingActionButton(
                  onPressed: () {}, // dummy button — does nothing
                  tooltip: 'Button 1',
                  child: const Icon(Icons.add),
                ),
                const SizedBox(width: 24),
                FloatingActionButton(
                  onPressed: () {}, // dummy button — does nothing
                  tooltip: 'Button 2',
                  child: const Icon(Icons.add),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
