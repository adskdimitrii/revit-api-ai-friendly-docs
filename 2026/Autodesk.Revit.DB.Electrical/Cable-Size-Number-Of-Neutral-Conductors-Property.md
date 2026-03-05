# Cable Size Number Of Neutral Conductors Property

Source: https://www.revitapidocs.com/2026/4fbf011b-96d8-bab1-e0aa-b4437064e5e4.htm

---

| Cable Size Number Of Neutral Conductors Property |
| --- |

The number of Neutral Conductors. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int NumberOfNeutralConductors { get; set; }
```

```
Public Property NumberOfNeutralConductors As Integer
	Get
	Set
```

```
public:
property int NumberOfNeutralConductors {
	int get ();
	void set (int value);
}
```

```
member NumberOfNeutralConductors : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for numberOfNeutralConductors is negative. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableSize Class](Cable-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
