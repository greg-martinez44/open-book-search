package Requests;


import java.io.IOException;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Get implements RequestInterface {
    public final OkHttpClient client;
    public String url;
    private Response response;

    public Get(String url) {
        this.client = new OkHttpClient();
        this.url = url;
    }

    public void run() throws IOException {
        Request request = new Request.Builder()
            .url(this.url)
            .build();
        this.response = this.getResponse(request);
    }

    private Response getResponse(Request request) throws IOException {
        Response response = this.client.newCall(request).execute();
        if (!response.isSuccessful()) {throw new IOException("Unexpected code " + response);}
        return response;
    }

    public Integer getResponseCode() {
        return this.response.code();
    }

    public JSONObject parseResponse() throws IOException, ParseException {
        String responseString = this.response.body().string();
        JSONParser parser = new JSONParser();
        return (JSONObject) parser.parse(responseString);
    }
}
