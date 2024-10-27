import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;
import java.sql.*;

public class JavaApplicationGUI extends JFrame implements ActionListener {

    private JTextArea outputTextArea;
    private JButton btnBasicExpressions, btnMethodWithParameters, btnExceptionHandling, btnLinkedList, btnIterator, btnWrapperAndAutoboxing, btnThread, btnFile, btnDatabase, btnVehicleInfo;
    private JLabel lblVehicleBrand;
    private JTextField txtVehicleBrand;

    public JavaApplicationGUI() {
        setTitle("Java Application GUI");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new GridLayout(4, 3));

        btnBasicExpressions = new JButton("Basic Expressions");
        btnMethodWithParameters = new JButton("Method with Parameters");
        btnExceptionHandling = new JButton("Exception Handling");
        btnLinkedList = new JButton("LinkedList Example");
        btnIterator = new JButton("Iterator Example");
        btnWrapperAndAutoboxing = new JButton("Wrapper & Autoboxing");
        btnThread = new JButton("Thread Example");
        btnFile = new JButton("File Example");
        btnDatabase = new JButton("Database Example");

        btnVehicleInfo = new JButton("Display Vehicle Info");
        lblVehicleBrand = new JLabel("Enter Vehicle Brand:");
        txtVehicleBrand = new JTextField(10);

        controlPanel.add(btnBasicExpressions);
        controlPanel.add(btnMethodWithParameters);
        controlPanel.add(btnExceptionHandling);
        controlPanel.add(btnLinkedList);
        controlPanel.add(btnIterator);
        controlPanel.add(btnWrapperAndAutoboxing);
        controlPanel.add(btnThread);
        controlPanel.add(btnFile);
        controlPanel.add(btnDatabase);

        JPanel vehiclePanel = new JPanel();
        vehiclePanel.setLayout(new FlowLayout());
        vehiclePanel.add(lblVehicleBrand);
        vehiclePanel.add(txtVehicleBrand);
        vehiclePanel.add(btnVehicleInfo);

        outputTextArea = new JTextArea(10, 50);
        outputTextArea.setEditable(false);

        JScrollPane scrollPane = new JScrollPane(outputTextArea);

        add(controlPanel, BorderLayout.NORTH);
        add(scrollPane, BorderLayout.CENTER);
        add(vehiclePanel, BorderLayout.SOUTH);

        btnBasicExpressions.addActionListener(this);
        btnMethodWithParameters.addActionListener(this);
        btnExceptionHandling.addActionListener(this);
        btnLinkedList.addActionListener(this);
        btnIterator.addActionListener(this);
        btnWrapperAndAutoboxing.addActionListener(this);
        btnThread.addActionListener(this);
        btnFile.addActionListener(this);
        btnDatabase.addActionListener(this);
        btnVehicleInfo.addActionListener(this);
    }


    private void displayOutput(String message) {
        outputTextArea.append(message + "\n");
    }

   
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnBasicExpressions) {
            basicExpressionsAndControlFlow();
        } else if (e.getSource() == btnMethodWithParameters) {
            methodWithParameters(5, 10);
        } else if (e.getSource() == btnExceptionHandling) {
            exceptionHandling();
        } else if (e.getSource() == btnLinkedList) {
            linkedListExample();
        } else if (e.getSource() == btnIterator) {
            iteratorExample();
        } else if (e.getSource() == btnWrapperAndAutoboxing) {
            wrapperAndAutoboxing();
        } else if (e.getSource() == btnThread) {
            threadExample();
        } else if (e.getSource() == btnFile) {
            fileExample();
        } else if (e.getSource() == btnDatabase) {
            databaseExample();
        } else if (e.getSource() == btnVehicleInfo) {
            String brand = txtVehicleBrand.getText();
            if (!brand.isEmpty()) {
                Vehicle vehicle = new Vehicle(brand);
                vehicle.displayInfo();
            } else {
                displayOutput("Please enter a vehicle brand.");
            }
        }
    }

    // Expression
    public void basicExpressionsAndControlFlow() {
        int a = 5;
        int b = 10;
        int result;

        result = (a < b) ? (a + b) : (a - b);

        displayOutput("Result: " + result);
    }

    // Method with parameters
    public void methodWithParameters(int x, int y) {
        displayOutput("Product of " + x + " and " + y + " is: " + (x * y));
    }

    // OOP - Object-oriented Programming
    public class Vehicle {
        private String brand;

        public Vehicle(String brand) {
            this.brand = brand;
        }

        public void displayInfo() {
            displayOutput("Brand of the vehicle: " + brand);
        }
    }

    // Exception handling
    public void exceptionHandling() {
            int a = 10;
            try {
                int c = a/0;
            }
            catch(ArithmeticException e){
                displayOutput("Divide by zero error " );

            }
     
    }

    // Data structures - LinkedList
    public void linkedListExample() {
        LinkedList<String> list = new LinkedList<>();
        list.add("Java");
        list.add("Python");
        list.add("C++");

        for (String lang : list) {
            displayOutput(lang);
        }
    }

    // Iterators
    public void iteratorExample() {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Orange");

        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            displayOutput(iterator.next());
        }
    }

    // Wrapper classes and autoboxing
    public void wrapperAndAutoboxing() {
        Boolean flag = true; // autoboxing
        displayOutput("Value of flag: " + flag);

        boolean value = flag; // unboxing
        displayOutput("Value: " + value);
    }

    // Threads
    public void threadExample() {
        Runnable task = () -> {
            for (int i = 0; i < 5; i++) {
                displayOutput("Thread running: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Thread thread = new Thread(task);
        thread.start();
    }

    // Files
    public void fileExample() {
        try (FileWriter writer = new FileWriter("output.txt")) {
            writer.write("Hello, World!");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Databases
    public void databaseExample() {
        String dbUrl = "jdbc:postgresql://localhost:5432/mydatabase";
        String username = "avin";
        String password = "vain";

        try (Connection conn = DriverManager.getConnection(dbUrl, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM mytable")) {

            while (rs.next()) {
                displayOutput("ID: " + rs.getInt("id") + ", Name: " + rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new JavaApplicationGUI().setVisible(true);
            }
        });
    }
}
