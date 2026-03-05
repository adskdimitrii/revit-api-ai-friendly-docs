# Temporary View Modes Accelerated Graphics Mode Property

Source: https://www.revitapidocs.com/2026/ea67f010-3a47-dee5-2225-96389399ab8a.htm

---

| Temporary View Modes Accelerated Graphics Mode Property |
| --- |

The current state of the Accelerated Graphics mode in the associated view. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool AcceleratedGraphicsMode { get; set; }
```

```
Public Property AcceleratedGraphicsMode As Boolean
	Get
	Set
```

```
public:
property bool AcceleratedGraphicsMode {
	bool get ();
	void set (bool value);
}
```

```
member AcceleratedGraphicsMode : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The Accelerated Graphics mode is either disabled or inapplicable in the associated view. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[TemporaryViewModes Class](Temporary-View-Modes-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
