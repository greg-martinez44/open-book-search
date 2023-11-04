package Requests;

import java.io.IOException;

import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

public interface RequestInterface {
    public void run() throws IOException;
    public Integer getResponseCode();
    public JSONObject parseResponse() throws IOException, ParseException;
}