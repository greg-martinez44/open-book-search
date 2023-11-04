package Requests;

import java.io.IOException;

import okhttp3.Response;

public interface RequestInterface {
    public void run();
    public Response getResponse() throws IOException;
}