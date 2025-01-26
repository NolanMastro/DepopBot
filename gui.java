import java.awt.*;
import java.io.*;
import javax.swing.*;

public class DepopBotGUI {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Depop Bot");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setLayout(new BorderLayout(10, 10));

        JPanel topPanel = new JPanel();
        topPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
        JButton statusButton = new JButton("Not Logged In");
        statusButton.setPreferredSize(new Dimension(150, 30));
        topPanel.add(statusButton);
        frame.add(topPanel, BorderLayout.NORTH);

        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        JLabel usernameLabel = new JLabel("Username:");
        gbc.gridx = 0;
        gbc.gridy = 0;
        centerPanel.add(usernameLabel, gbc);

        JTextField usernameField = new JTextField(20);
        gbc.gridx = 1;
        gbc.gridy = 0;
        centerPanel.add(usernameField, gbc);

        JLabel emailLabel = new JLabel("Email:");
        gbc.gridx = 0;
        gbc.gridy = 1;
        centerPanel.add(emailLabel, gbc);

        JTextField emailField = new JTextField(20);
        gbc.gridx = 1;
        gbc.gridy = 1;
        centerPanel.add(emailField, gbc);

        JLabel passwordLabel = new JLabel("Password:");
        gbc.gridx = 0;
        gbc.gridy = 2;
        centerPanel.add(passwordLabel, gbc);

        JPasswordField passwordField = new JPasswordField(20);
        gbc.gridx = 1;
        gbc.gridy = 2;
        centerPanel.add(passwordField, gbc);

        frame.add(centerPanel, BorderLayout.CENTER);

        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new GridLayout(1, 4, 10, 10));

        JButton submitButton = new JButton("Submit");
        bottomPanel.add(submitButton);

        JButton fillerButton1 = new JButton("Filler Button 1");
        bottomPanel.add(fillerButton1);

        JButton fillerButton2 = new JButton("Filler Button 2");
        bottomPanel.add(fillerButton2);

        JButton fillerButton3 = new JButton("Filler Button 3");
        bottomPanel.add(fillerButton3);

        frame.add(bottomPanel, BorderLayout.SOUTH);

        submitButton.addActionListener(e -> {
            String username = usernameField.getText();
            String email = emailField.getText();
            String password = new String(passwordField.getPassword());

            if (!username.isEmpty() && !email.isEmpty() && !password.isEmpty()) {
                JOptionPane.showMessageDialog(frame, "Login successful for: " + username);
                statusButton.setText("Logged In");

                System.out.println("Username: " + username);
                System.out.println("Email: " + email);
                System.out.println("Password: " + password);

                try {
                    
                    ProcessBuilder processBuilder = new ProcessBuilder("python", "login.py", username, email, password);
                    processBuilder.redirectErrorStream(true);
                    Process process = processBuilder.start();

                    
                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        System.out.println("Python output: " + line);
                    }

                    process.waitFor();

                } catch (IOException | InterruptedException ex) {
                    ex.printStackTrace();
                    JOptionPane.showMessageDialog(frame, "Error executing login.py", "Error", JOptionPane.ERROR_MESSAGE);
                }

            } else {
                JOptionPane.showMessageDialog(frame, "Please fill in all fields.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        frame.setVisible(true);
    }
}
