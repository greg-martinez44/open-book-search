package Requests;

import java.io.IOException;
import java.util.List;

import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import okhttp3.Response;

public class GetTest {

    private final String BASE_URL = "https://www.loc.gov";
    private final String RETURN_FORMAT_FLAG = "fo=json";

    @Test
    void testGetResponseCode() throws IOException {
        String url = this.BASE_URL + "/search/q=baseball&at=results&" + this.RETURN_FORMAT_FLAG;
        Get get = new Get(url);
        get.run();
        Integer expected = 200;
        Integer actual = get.getResponseCode();
        assertEquals(expected, actual);
    }

    @Test
    void testParseResponse() throws IOException, ParseException {
        String url = this.BASE_URL + "/search/q=baseball&at=results&" + this.RETURN_FORMAT_FLAG;
        Get get = new Get(url);
        get.run();
        JSONObject actual = get.parseResponse();
        assertNotNull(actual);
    }

}
