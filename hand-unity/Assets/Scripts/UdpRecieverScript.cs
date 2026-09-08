using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class UdpRecieverScript : MonoBehaviour
{

    private UdpClient udpClient; // hold connection
    public int listenPort = 5005; // can change in inspector because private
    public string receivedData = "None";

    void Start()
    {
        try
        {
            // initalize and bind udp client
            udpClient = new UdpClient(listenPort);

            // start listening
            StartListening();
            Debug.Log($"UDP Receiver started on port {listenPort}");
        }
        catch (Exception e)
        {
            Debug.Log($"Failed to start UDP client: {e.Message}");
        }
        
    }

    private void StartListening()
    {
        // .Receive is stop code while waiting, .BeginReceive is wait in the background 
        udpClient.BeginReceive(ReceiveCallback, null); // what to do, what else to return
    }

    private void ReceiveCallback(IAsyncResult ar) // ar = result
    {
        try
        {
            // get IP address of package
            IPEndPoint remoteEP = new IPEndPoint(IPAddress.Any, 0);

            // get the sent bytes
            byte[] receivedBytes = udpClient.EndReceive(ar, ref remoteEP);
            
            // convert bytes to a string
            receivedData = Encoding.UTF8.GetString(receivedBytes);

            Debug.Log($"Received from {remoteEP}: {receivedData}");

            StartListening();
        }
        catch (ObjectDisposedException)
        {
            // Expected when the socket is closed on shutdown
        }
        catch (Exception e)
        {
            Debug.Log($"UDP Receive Error: {e.Message}");
        }
    }

    void OnDestroy()
    {
        // Crucial: Clean up and close the port when the script or game stops
        if (udpClient != null)
        {
            udpClient.Close();
        }
    }
}
