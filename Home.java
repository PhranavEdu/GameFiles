import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
//@Scope(value="prototype")      //we can call object many times using with prototype scope

public class Home {
public Home() {
	System.out.println("Home Home");
	}
	//POJO class
	private String owner;
	private int doorNo;
	@Autowired
	@Qualifier("III")
	private InternetConnection modem;     // modem object
	public String getOwner() {
		return owner;
	}
	public void setOwner(String owner) {
		this.owner = owner;
	}
	public int getDoorNo() {
		return doorNo;
	}
	public void setDoorNo(int doorNo) {
		this.doorNo = doorNo;
	}
	
	public void connect() {
		
		modem.switchOn();
		System.out.println("Connecting to Internet");
	}
	
}
