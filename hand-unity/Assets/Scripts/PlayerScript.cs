using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class PlayerScript : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI playerText;
    [SerializeField] UdpRecieverScript receiver;
    [SerializeField] GameManager gameManager;

    private Dictionary<string, string> emojis = new()
        {
            ["Open_Palm"]="✋", ["Victory"]="✌️", ["Closed_Fist"]="✊",
            ["Thumb_Up"]="👍", ["Thumb_Down"]="👎", ["ILoveYou"]="🤟",
            ["Pointing_Up"]="👆", ["None"]=""
        };


    void Start()
    {
        playerText.text = "";
    }

    void Update()
    {
        string data = receiver.receivedData;
        Debug.Log("Data: ");
        Debug.Log(data);
        playerText.text = emojis[data];
    }
}