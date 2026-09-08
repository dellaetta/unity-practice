using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.Controls;
using System.Collections.Generic;
using System.Linq;
using TMPro;

public class GuideScript : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI guideText;
    [SerializeField] GameManager gameManager;
    [SerializeField] UdpRecieverScript receiver;

    private int count;
    private string targetEmojiText;
    private Dictionary<string, string> emojis = new()
        {
            ["Open_Palm"]="✋", ["Victory"]="✌️", ["Closed_Fist"]="✊",
            ["Thumb_Up"]="👍", ["Thumb_Down"]="👎", ["ILoveYou"]="🤟",
            ["Pointing_Up"]="👆"
        };

    void Start()
    {
        count = 0;

        // set target emoji
        setRandom();
    }

    void Update()
    {   
        string data = receiver.receivedData;
        if (data != "None" && data == targetEmojiText)
        {
            count += 1;
            
            if ( count > 50 )
            {
                setRandom();
                gameManager.PlayerScored();
                count = 0;
            }
        }
        else
        {
            count = 0;
        }
    }

    private void setRandom()
    {
        targetEmojiText = emojis.Keys.ElementAt(Random.Range(0, emojis.Count));
        guideText.text = emojis[targetEmojiText];
;    }
}