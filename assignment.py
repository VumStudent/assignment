package newproject;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
public class PG9 {
    public static void main(String[] args) {
        System.setProperty("webdriver.firefox.marionette","C:\\geckodriver.exe");
        String baseUrl = "http://mdn.mozillademos.org/files/3698/image_upload_preview.html";
        WebDriver driver = new FirefoxDriver();

        driver.get(baseUrl);
        WebElement uploadElement = driver.findElement(By.id("uploadImage"));

        uploadElement.sendKeys("C:\\‪Users\\student\\Downloads\\picture.jpg");
    
        driver.findElement(By.value("Send")).click();
        }
}
