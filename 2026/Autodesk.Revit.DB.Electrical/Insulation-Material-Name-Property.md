# Insulation Material Name Property

Source: https://www.revitapidocs.com/2026/2fd2ab3c-a9a0-6feb-bc5a-c485cc3d918c.htm

---

| Insulation Material Name Property |
| --- |

The Conductor Insulation Material name. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string Name { get; set; }
```

```
Public Property Name As String
	Get
	Set
```

```
public:
property String^ Name {
	String^ get ();
	void set (String^ value);
}
```

```
member Name : string with get, set
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: name is an empty string or contains only whitespace.  \-or\-  When setting this property: name cannot include prohibited characters, such as "{, }, \[, ], \|, ;, less\-than sign, greater\-than sign, ?, \`, \~".  \-or\-  When setting this property: name is not unique in document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[InsulationMaterial Class](Insulation-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
