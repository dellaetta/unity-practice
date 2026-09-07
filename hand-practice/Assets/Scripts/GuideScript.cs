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

    private Key[] keys = { Key.A, Key.W, Key.S, Key.D, Key.K, Key.L, Key.F };
    private Dictionary<string, string> emojis = new()
        {
            ["Open_Palm"]="✋", ["Victory"]="✌️", ["Closed_Fist"]="✊",
            ["Thumb_Up"]="👍", ["Thumb_Down"]="👎", ["ILoveYou"]="🤟",
            ["Pointing_Up"]="👆"
        };
    private Key targetKey;
    private string targetEmoji;

    void Start()
    {
        // Set the target key
        targetKey = keys[Random.Range(0, keys.Length)];
        targetEmoji = emojis.Keys.ElementAt(Random.Range(0, emojis.Count));
        guideText.text = emojis[targetEmoji];
    }

    void Update()
    {
        // Check for target key
        bool pressed = targetKey switch
        {
            Key.A => Keyboard.current.aKey.wasPressedThisFrame,
            Key.W => Keyboard.current.wKey.wasPressedThisFrame,
            Key.S => Keyboard.current.sKey.wasPressedThisFrame,
            Key.D => Keyboard.current.dKey.wasPressedThisFrame,
            Key.K => Keyboard.current.kKey.wasPressedThisFrame,
            Key.L => Keyboard.current.lKey.wasPressedThisFrame,
            Key.F => Keyboard.current.fKey.wasPressedThisFrame,
            _ => false
        };
        
        // If pressed do necessary actions
        if (pressed)
        {
            targetKey = keys[Random.Range(0, keys.Length)];
            guideText.text = targetKey.ToString();
            gameManager.PlayerScored();
        }
    }
}