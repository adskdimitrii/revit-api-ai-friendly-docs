# IFCParameter Template Set Property Set Applicable Entities Method

Source: https://www.revitapidocs.com/2026/d991aec4-fd99-316c-f482-6207c1cd26a3.htm

---

| IFCParameter Template Set Property Set Applicable Entities Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetPropertySetApplicableEntities(
	PropertySetupType propertySetupType,
	string propertySetName,
	IList<string> applicableEntities
)
```

```
Public Sub SetPropertySetApplicableEntities ( 
	propertySetupType As PropertySetupType,
	propertySetName As String,
	applicableEntities As IList(Of String)
)
```

```
public:
void SetPropertySetApplicableEntities(
	PropertySetupType propertySetupType, 
	String^ propertySetName, 
	IList<String^>^ applicableEntities
)
```

```
member SetPropertySetApplicableEntities : 
        propertySetupType : PropertySetupType * 
        propertySetName : string * 
        applicableEntities : IList<string> -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
propertySetName String
applicableEntities IList String

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
