# Parameter Description Property

Source: https://www.revitapidocs.com/2026/2e258549-0d71-8e2d-56c4-130e890362a3.htm

---

| Parameter Description Property |
| --- |

Returns the tooltip information for a parameter. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string Description { get; set; }
```

```
Public Property Description As String
	Get
	Set
```

```
public:
property String^ Description {
	String^ get ();
	void set (String^ value);
}
```

```
member Description : string with get, set
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this parameter is built\-in. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Parameter Class](Parameter-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
