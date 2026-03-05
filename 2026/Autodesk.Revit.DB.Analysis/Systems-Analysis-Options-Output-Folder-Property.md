# Systems Analysis Options Output Folder Property

Source: https://www.revitapidocs.com/2026/d980a989-f63a-17a4-b431-596b8884afb5.htm

---

| Systems Analysis Options Output Folder Property |
| --- |

The path of the output folder for systems analysis. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string OutputFolder { get; set; }
```

```
Public Property OutputFolder As String
	Get
	Set
```

```
public:
property String^ OutputFolder {
	String^ get ();
	void set (String^ value);
}
```

```
member OutputFolder : string with get, set
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The analysis requires a valid output folder path or empty string. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When requesting a new system analysis, it is okay to have an empty output folder in the SystemsAnalysisOption. In that case,
 the ViewSystemsAnalysisReport would supply the output folder, typically at the system TEMP folder. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemsAnalysisOptions Class](8d8fe6a8-d3f6-c4fd-99ac-3181ba0253d6.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
